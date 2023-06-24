

reformat that:
    text = edit.selected_text()
    user.format_sentences(text)


replay line:
    edit.select_line()
    text = edit.selected_text()
    user.replay_line(text)

compare line: 
    edit.select_line()
    text = edit.selected_text()
    user.compare_line(text)

