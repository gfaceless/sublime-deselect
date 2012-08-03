import sublime, sublime_plugin

# Add a keybinding for deselect set to enter
class DeselectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Grab start and end points of selection. If there
        # are multiple selections, take the first one, consistent
        # with the behavior of Sublime's single_selection().
        start = self.view.sel()[0].a
        end = self.view.sel()[0].b

        # Point the cursor at the start point of the region.
        cursorLocation = sublime.Region(start, start)

        # Clear out the view and add the cursor location.
        self.view.sel().clear()
        self.view.sel().add(cursorLocation)
