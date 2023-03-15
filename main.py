import markdown


def bionic():
    # opening and reading a text file
    try:
        with open('sample_text.txt', 'r') as sample:
            contents = sample.read()
    except FileNotFoundError as error:
        print(error)

    # split into list of words
    word_list = contents.split()
    # create new empty list
    output_list = []

    # convert the words and add to a list
    for i in range(len(word_list)):
        word = word_list.pop(0)
        # do the operation on the word
        if len(word) == 1:
            final_word = f'**{word}**'
        elif len(word) % 2 == 0:
            final_word = '**{}{}**'.format(
                word[0], word[1:int(len(word)/2)]) + word[int(len(word)/2):]
        elif len(word) % 2 != 0:
            final_word = '**{}{}**'.format(
                word[0], word[1:int(len(word)/2) + 1]) + word[int(len(word)/2)+1:]
        output_list.append(final_word)

    # join the words of the list
    output = ' '.join(output_list)

    # open/create markdown file
    with open('bionic.md', 'w') as bionic:
        # write it with contents
        bionic.write(output)

    # Open the markdown file
    with open('bionic.md', 'r') as md_file:
        # Read the contents of the file
        md_contents = md_file.read()

    # Convert the markdown to HTML
    html_contents = markdown.markdown(md_contents)

    # Open an HTML file and write the converted contents
    with open('bionic.html', 'w') as html_file:
        html_file.write(html_contents)


bionic()
