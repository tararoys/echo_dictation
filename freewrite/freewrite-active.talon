mode: user.echo

-
tag() = user.record_replay
^press <user.modifiers>$: key(modifiers)
^press <user.keys>$: key(keys)

# Everything here should call `user.dictation_insert()` instead of `insert()`, to correctly auto-capitalize/auto-space.
<user.raw_prose>:
    tex = "             |"
    user.replay_save_last()
    text = clip.text()
    teext= tex + text 
    text2 =  teext + "\n"
    teeext = user.dictation_formatter_format(raw_prose)
    teeeext = text2 + teeext
    clip.set_text(teeeext)
    #user.dictation_insert(teeeext)
    #user.vscode("rainbow-csv.Align")
    sleep(200ms)
    edit.paste()
    key(insert:down c insert:up)

^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
    mode.disable("user.echo")