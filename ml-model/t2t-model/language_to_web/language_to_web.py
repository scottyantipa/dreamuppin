from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry

#
# Generates language -> html example input/output.
#

# <p />
def paragraph(add_pair, num_per_type):
    template = "A paragraph with the text '{0}'"
    for value in range(num_per_type):
        text = value
        input = template.format(text)
        output = "<p>{0}</p>".format(text)
        add_pair(input, output)

# <img />
def img(add_pair, num_per_type):
    template = "An image with the src '{0}'"
    for value in range(num_per_type):
        text = value
        input = template.format(text)
        output = '<img src="{0}" />'.format(text)
        add_pair(input, output)

# <strong />
def strong(add_pair, num_per_type):
    template = "Bold text with the words '{0}'"
    for value in range(num_per_type):
        text = value
        input = template.format(text)
        output = '<strong>{0}</strong>'.format(text)
        add_pair(input, output)

def video(add_pair, num_per_type):
    template = "An mp4 video from the source '{0}'."
    for value in range(num_per_type):
        text = value
        input = template.format(text)
        output = '<video src="{0}" type="video/mp4"/>'.format(text)
        add_pair(input, output)

# <span style="color...">...</span>
def color_txt(add_pair, num_per_type):
    templates = [
        "{1} text with the sentence {0}",
        "In a {1} font put the words {0}",
        "The sentence {0} in a {1} color",
    ]
    colors = ['red', 'blue', 'green', 'yellow', 'FF12A1', 'orange']
    for template in templates:
        for color in colors:
            for value in range(num_per_type):
                text = value
                input = template.format(text, color)
                output = '<span style="color: {1}">{0}</span>'.format(text, color)
                add_pair(input, output)

# <img src="..." style="width...height..." />
def img_dimensions(add_pair, num_per_type):
    templates = [
        "An image with the source 'google.com' and width of {0} and height of {1}"
    ]
    for template in templates:
        for width in range(num_per_type):
            for height in range(num_per_type):
                input = template.format(width, height)
                output = '<img src="google.com" style="width: {0}; height: {1}" />'.format(width, height)
                add_pair(input, output)

# TODO XXX make own package
def make_corpus(num_per_type):
    inputs = []
    outputs = []
    def add_pair(input, output):
        inputs.append(input)
        outputs.append(output)

    paragraph(add_pair, num_per_type)
    img(add_pair, num_per_type)
    strong(add_pair, num_per_type)
    video(add_pair, num_per_type)
    color_txt(add_pair, num_per_type)
    img_dimensions(add_pair, num_per_type)

    return [inputs, outputs]

# A t2t seq2seq problem for translating language -> html
# Inspiration https://tensorflow.github.io/tensor2tensor/new_problem.html
@registry.register_problem
class LanguageToWeb(text_problems.Text2TextProblem):
    '''Converts natural language to HTML'''

    @property
    def approx_vocab_size(self):
        # This was copy / pasted
        return 2**13  # ~8k
    @property
    def is_generate_per_split(self):
        # generate_data will shard the data into TRAIN and EVAL for us.
        return False

    @property
    def dataset_splits(self):
        """Splits of data to produce and number of output shards for each."""
        # 10% evaluation dataset
        return [{
            "split": problem.DatasetSplit.TRAIN,
            "shards": 9,
        }, {
            "split": problem.DatasetSplit.EVAL,
            "shards": 1,
        }]

    def generate_samples(self, data_dir, tmp_dir, dataset_split):
        del data_dir
        del tmp_dir
        del dataset_split

        # HACK There are two ways this problem can generate data. Manually change
        # this bool to switch between them. The first is generated english/code pairs. The
        # second is from files that come from human written english describing genrated html.
        if False:
            # Use fake generated data
            inputs, outputs = make_corpus(10)
            for i in range(len(inputs)):
                yield {
                    "inputs": inputs[i],
                    "targets": outputs[i]
                }
        else:
            # Use data from files. The `small-data` dir is .git-ignored in this repo and must be
            # provided by the caller. The `/floyd/home` dir is the dir from which the floyd run
            # is launched.
            inputs_file = open('/floyd/home/small-data/video-tag-1000/inputs.txt', 'r')
            outputs_file = open('/floyd/home/small-data/video-tag-1000/outputs.txt', 'r')

            for input in inputs_file:
                if len(input) == 0:
                    continue
                output = outputs_file.readline()
                yield {
                    "inputs": input,
                    "targets": output
                }
