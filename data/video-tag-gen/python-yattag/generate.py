import os
from faker import Faker
import random
from math import floor, ceil
import argparse
from bs4 import BeautifulSoup

# Generates random <video /> tags.
# Note that this may generate valid but non-optimal tags, like now following guidelines:
# https://developers.google.com/web/updates/2017/09/autoplay-policy-changes

fake = Faker()

def fake_video_src():
    url = fake.url()
    file_name = fake.word() + '.mp4'
    return file_name # _TODO_
    return url + file_name

def fake_img_src():
    url = fake.url()
    file_type = '.png' if randbool() else '.jpg'
    file_name = fake.word() + file_type
    return file_name # _TODO_
    return url + file_name

def semirand(threshold):
    return random.random() > threshold

def randbool():
    return random.choice([True, False])

def randsize():
    if semirand(0.1):
        percent = random.choice([25, 50, 75, 100])
        return "{0}%".format(ceil(percent))
    else:
        pixels = []
        for i in range(10):
            pixels.append(i * 100)
        return "{0}px".format(random.choice(pixels))

# param attrs Attributes to include in the video tag
def generate(attrs):
    keyword_args = {
        "src": fake_video_src(),
        "poster": fake_img_src() if ('poster' in attrs and randbool()) else None,
        "controls": "true" if ("controls" in attrs and semirand(0.25)) else None,
        "autoplay": "true" if ("autoplay" in attrs and randbool()) else None,
        "muted": "true" if ("muted" in attrs and randbool()) else None,
        "loop": "true" if ("loop" in attrs and randbool()) else None,
        "width": randsize() if ("width" in attrs and randbool()) else None,
        "height": randsize() if ("height" in attrs and randbool()) else None
    }
    # strip out Nones
    tag_attrs = {k: v for k, v in keyword_args.items() if v is not None}
    attr_keys = tag_attrs.keys()

    # make node using bs4
    soup = BeautifulSoup('', 'html5lib')
    body = soup.body
    el = soup.new_tag('video')
    if 'src' in attr_keys:
        el['src'] = tag_attrs['src']
    if 'poster' in attr_keys:
        el['poster'] = tag_attrs['poster']
    # Use None so the output looks like 'autoplay' not 'autoplay=""'
    if 'controls' in tag_attrs:
        el['controls'] = None
    if 'autoplay' in attr_keys:
        el['autoplay'] = None
    if 'muted' in attr_keys:
        el['muted'] = None
    if 'loop' in tag_attrs:
        el['loop'] = None
    if 'width' in attr_keys:
        el['width'] = tag_attrs['width']
    if 'height' in attr_keys:
        el['height'] = tag_attrs['height']


    # make english hints
    input_str = 'a video'
    for attr, val in tag_attrs.items():
        if attr in ['src', 'poster', 'width', 'height']:
            input_str += ' with a {0} of "{1}"'.format(attr, val)
        else: # bools, no val
            input_str += ' with {}'.format(attr)

    return [
        input_str,
        str(el)
    ]

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--count', type=int, help='number of examples to generate')
    args = arg_parser.parse_args()
    attrs = ["controls", "autoplay", "poster", "width", "height", "muted"]
    lines = [generate(attrs) for i in range(args.count)]
    dir_name = "xyz-{}-{}".format('-'.join(attrs), args.count)
    os.makedirs(dir_name)
    english_writer = open("{}/english.txt".format(dir_name), 'a')
    code_writer = open("{}/html.txt".format(dir_name), 'a')
    for l in lines:
        english_writer.write(l[0] + '\n')
        code_writer.write(l[1] + '\n')
    code_writer.close()
    english_writer.close()
