from yattag import Doc
from faker import Faker
import random
from math import floor, ceil

# Generates random <video /> tags.
# Note that this may generate valid but non-optimal tags, like now following guidelines:
# https://developers.google.com/web/updates/2017/09/autoplay-policy-changes

fake = Faker()

def fake_video_src():
    url = fake.url()
    file_name = fake.word() + '.mp4'
    return url + file_name

def fake_img_src():
    url = fake.url()
    file_type = '.png' if randbool() else '.jpg'
    file_name = fake.word() + file_type
    return url + file_name

def semirand(threshold):
    return random.random() > threshold

def randbool():
    return random.choice([True, False])

def randsize(is_height=False):
    if semirand(0.1):
        percent = random.choice([25, 50, 75, 100])
        return "{0}%".format(ceil(percent))
    else:
        pixels = []
        for i in range(10):
            pixels.append(i * 100)
        return "{0}px".format(random.choice(pixels))

# test_src = "https://www.w3schools.com/tags/movie.mp4"

def generate():
    keyword_args = {
        "src": fake_video_src(),
        "poster": fake_img_src() if randbool() else None,
        "controls": "true" if semirand(0.05) else None,
        "autoplay": "true" if randbool() else None,
        "muted": "true" if randbool() else None,
        "loop": "true" if randbool() else None,
        "width": randsize() if randbool() else None,
        "height": randsize() if randbool() else None
    }

    # unfortunately yattag doesnt support boolean attributes very well
    # so you cant do <video autoplay/> you have to do <video autoplay='true'/>
    # TODO randomize the order of the attributes
    without_none_args = {k: v for k, v in keyword_args.items() if v is not None}

    doc, tag, text = Doc().tagtext()
    with tag('video', **without_none_args):
        text('')
    print(doc.getvalue())

for i in range(100):
    generate()
