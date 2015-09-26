import sublime, sublime_plugin
import subprocess

def search(q):
    settings = sublime.load_settings('sublime_hsp.sublime-settings')
    helpman = settings.get('hsp_dir', '') + '/hdl.exe'
    subprocess.Popen([helpman, q])

class HdlSearchCommand(sublime_plugin.TextCommand):
    """
    Search the selected text or the current word
    """
    def run(self, edit):
        querys = []
        for region in self.view.sel():
            if region.empty():
                # if we have no selection grab the current word
                word = self.view.word(region)
                if not word.empty():
                    querys.append(self.view.substr(word))
            else:
                # append the selection
                if not region.empty():
                    querys.append(self.view.substr(region))

        if len(querys) != 0:
            selection = " ".join(querys)
            search(querys[0])
        else:
            sublime.status_message(" Nothing to search !")
            print("HDL: Nothing to search !")
