from talon import Context, Module, actions, app, clip, imgui, settings, ui

ctx = Context()
mod = Module()

mod.mode('echo', "method of dictating phrase by phrase where you say a phrase and a screen reader technology echoes it back")

@mod.action_class
class Actions:
    def format_sentences(file: str):
        """Takes a freewrite transcript and creates a file sentences out of it, one line per sentence"""
        line_list = file.split('\n')
        for indx, line in enumerate(line_list):
 
            utterance = line.split("|", 1)[0].rstrip()
            if(not utterance):
                line_list[indx] = "\n\n"
            else:
                line_list[indx] = utterance

        file = " ".join(line_list)
        line_list = file.split(' .')
        file = ".".join(line_list)
        line_list = file.split(' !')
        file = "!".join(line_list)
        line_list = file.split(' ?')
        file = "?".join(line_list)
        line_list = file.split(' ,')
        file = ",".join(line_list)
        clip.set_text(file)
    
    def format_paragraphs():
        """Takes a list of sentences and makes them into paragraphs based on whether there is a blank space."""

    def replay_line(file: str):
        """Replay the flac file used to create this line."""
        utterance = str(file.split("|",1)[1].rstrip())
        print(utterance + " >>>>>>>>>>>>>>>>")
        actions.user.replay_saved_file_by_file_name(utterance)

    def compare_line(file: str):
        """Replay the flac file used to create this line."""
        utterance = str(file.split("|",1)[1].rstrip())
        caption = str(file.split("|",1)[0].rstrip())
        print(utterance + " >>>>>>>>>>>>>>>>")
        actions.user.replay_saved_file_by_file_name(utterance)
        clip.set_text(caption)
        actions.key("insert:down c insert:up")