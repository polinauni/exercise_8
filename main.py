#Exercise 08
#1

def write_to_file(text, output_file_path):
    try:
        with open(output_file_path, 'x') as output_file:
            output_file.write(text)
    except FileExistsError:
        raise RuntimeError('Output file already exists!')
    with open(output_file_path, 'w') as f:
        f.write(text)

#2

import spacy

def count_stopwords(input_file_path):
    nlp = spacy.load('en_core_web_sm')
    stop_words = nlp.Defaults.stop_words
    count = 0
    with open(input_file_path, 'r') as f:
        for line in f:
            doc = nlp(line)
            count += len([word for word in doc if word.text.lower() in stop_words])
    return count

#3

def remove_stopwords(input_file_path, output_file_path):
    nlp = spacy.load('en_core_web_sm')
    with open(input_file_path, 'r') as f_in, open(output_file_path, 'w') as f_out:
        doc = nlp(f_in.read())
        stopwords = nlp.Defaults.stop_words
        for token in doc:
            if not token.is_stop:
                f_out.write(token.text + ' ')
            else:
                stopwords.remove(token.text)
        nlp.Defaults.stop_words = stopwords

#4

def tokenize_text(input_file_path, output_file_path):
    nlp = spacy.load('en_core_web_sm')
    with open(input_file_path, "r") as f_in, open(output_file_path, "w") as f_out:
        doc = nlp(f_in.read())

        for token in doc:
            f_out.write(f"{token.text: {10}}{token.pos_:{10}}{token.dep_:{10}}\n")


#5

from spacy import displacy

def save_visualization(input_file_path, output_file_path):
    nlp = spacy.load('en_core_web_sm')
    with open(input_file_path, 'r') as f:
        text = f.read()
        doc = nlp(text)
        svg = displacy.render(doc)
        with open(output_file_path, 'w') as f_out:
            f_out.write(svg)
        displacy.serve(doc)

input_file_path = 'input.txt'
output_file_path = 'output.svg'

with open(input_file_path, 'w') as f:
    f.write("Hello, I'm Polina and I'm 23 years old.")

save_visualization(input_file_path, output_file_path)








