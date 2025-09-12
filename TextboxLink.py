from webbrowser import open_new as open_link
from tkinter import Tk, Toplevel, Label, font
class TextboxLink():
    """
    Author: Kevin Glentworth
    Date: August-2025
    Adds clickable URLs to a textbox..
    __init__ sets the initial values for each configurable item, colours etc.
    .config allows those values to be changed for any future calls, but not for existing links and words.
    .add allows the options to be changed for that item only.
    The textbox is passed in the .add function, rather than the __init__ function.
    """
    def __init__(self,
                 underline: bool=True,
                 underlinefg: str='blue',
                 hover_ul: str='green',
                 hover_bg: str='orange',
                 fg_color: str='blue',
                 bg_color: str='yellow',
                 popup_fg: str='blue',
                 popup_bg: str = 'lightyellow',
                 popup_border: str = 'red',
                 popup_font: list = ('Code New Roman', 13),
                 show_url: bool = True):
        self._underline = underline
        self._underlinefg = underlinefg
        self._hover_ul = hover_ul
        self._hover_bg = hover_bg
        self._fg_color = fg_color
        self._bg_color = bg_color
        self._popup_fg = popup_fg
        self._popup_bg = popup_bg
        self._popup_border = popup_border
        self._popup_font = popup_font
        self._show_url = show_url

        
    def show_url_popup(self, text_widget, message, p_fg: str='blue', p_bg: str='lightyellow', p_bd: str='red', p_font: list = None):
        """
        Shows the URL of the link under the mouse.

        If the mouse pointer ends up over the popup object, it is treated as an <Exit>, which closes the popup window.
        As the mouse is still within the text_widget, it then performs another <Enter> and goes into a loop until the mouse is
        moved off the popup. Adjust both x and y to keep the popup away from the mouse cursor.
        The popup_border isn't a Label widget item, it is applied to the Toplevel widget with padding, to make it appear
        as a border colour.
        """
        mouse_x = self._text_widget.winfo_pointerx() + 10
        mouse_y = self._text_widget.winfo_pointery() - 30

        self.popup = Toplevel(self._text_widget, bg=p_bd, padx=2, pady=2) # padx & pady allow the colour to show around the label.
        self.popup.overrideredirect(True)
        self.popup.geometry(f'+{mouse_x}+{mouse_y}')
        self.popup.attributes('-topmost', True) # Ensure the popup is above everything else.

        Label(self.popup, text=message, fg=p_fg, bg=p_bg, relief='flat', borderwidth=0, padx=2, pady=2, font=p_font).pack()

        
    def kill_url_popup(self):
        self.popup.destroy()


    def add(self,
            text_widget,
            the_text: str,
            tag_name: str,
            the_link: str,
            new_text: str = None,
            underline: bool=None,
            underlinefg: str=None,
            hover_ul: str=None,
            hover_bg: str=None,
            fg_color: str=None,
            bg_color: str=None,
            popup_fg: str=None,
            popup_bg: str=None,
            popup_border: str=None,
            popup_font: list = None,
            show_url: bool = None):
        """
        Highlight text and create a link in a text widget that supports tags. The parameters here over-ride those
        set in __init__, but only for this call.
        To change the colours for future calls, use config.
        """
        try:
            text_widget.tag_add('????',1.0, 'end')
        except AttributeError:
            raise Exception(f'item {text_widget} does not support tags.')
        text_widget.tag_delete('????')
        str0: str = text_widget.get('1.0', 'end')
        if len(str0) == 0:
            return
        if (text_length := len(the_text)) == 0:
            return
        if (find_location := str0.find(the_text)) == -1:
            return
        begin_pos = '1.0 linestart+' + str(find_location) + 'c'
        if new_text is not None and len(new_text) > 0:
            end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
            text_widget.configure(state='normal')
            text_widget.delete(begin_pos, end_pos)
            text_widget.insert(begin_pos, new_text)
            text_widget.configure(state='disabled')
            text_length = len(new_text)
            str0 = text_widget.get('1.0', 'end') # reload text from widget rather than slicing str0
        end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
        self._text_widget = text_widget
        # Temporary variables are named as the actual variable with an _ appended.
        fg_color_ = self._fg_color if fg_color is None else fg_color
        bg_color_ = self._bg_color if bg_color is None else bg_color
        underline_ = self._underline if underline is None else underline
        underlinefg_ = self._underlinefg if underlinefg is None else underlinefg
        hover_ul_ = self._hover_ul if hover_ul is None else hover_ul
        hover_bg_ = self._hover_bg if hover_bg is None else hover_bg
        popup_fg_ = self._popup_fg if popup_fg is None else popup_fg
        popup_bg_ = self._popup_bg if popup_bg is None else popup_bg
        popup_border_ = self._popup_border if popup_border is None else popup_border
        popup_font_ = self._popup_font if popup_font is None else popup_font
        show_url_ = self._show_url if show_url is None else show_url
        text_widget.tag_add(tag_name, begin_pos, end_pos)
        text_widget.tag_config(tag_name, foreground=fg_color_, background=bg_color_)
        if underline_:
            text_widget.tag_config(tag_name, underline=True, underlinefg=underlinefg_)
        text_widget.tag_bind(tag_name, '<Button-1>', lambda x: open_link(the_link))
        """
        Need to define the cursor, the colours and the action for <Enter> and <Leave>. We pass an embedded
        list or tuple of commands to the lambda for this, we cannot use a list variable or a tuple variable.
        """
        if show_url_:
            text_widget.tag_bind(tag_name, '<Enter>',
                                 lambda x: [text_widget.configure(cursor='hand2'),
                                            text_widget.tag_config(tag_name, underlinefg=hover_ul_, background=hover_bg_),
                                            self.show_url_popup(self._text_widget, the_link, popup_fg_, popup_bg_, popup_border_, popup_font_)])
            text_widget.tag_bind(tag_name, '<Leave>',
                                 lambda x: [text_widget.configure(cursor='xterm'),
                                            text_widget.tag_config(tag_name, underlinefg=underlinefg_, background=bg_color_),
                                            self.kill_url_popup()])
        else:
            text_widget.tag_bind(tag_name, '<Enter>',
                                 lambda x: [text_widget.configure(cursor='hand2'),
                                            text_widget.tag_config(tag_name, underlinefg=hover_ul_, background=hover_bg_)])
            text_widget.tag_bind(tag_name, '<Leave>',
                                 lambda x: [text_widget.configure(cursor='xterm'),
                                            text_widget.tag_config(tag_name, underlinefg=underlinefg_, background=bg_color_)])


    def configure(self, **kwargs):
        self.config(**kwargs)
        
        
    def config(self, **kwargs):
        if 'underline' in kwargs:
            self._underline = kwargs.pop('underline')
        if 'underlinefg' in kwargs:
            self._underlinefg = kwargs.pop('underlinefg')
        if 'hover_ul' in kwargs:
            self._hover_ul = kwargs.pop('hover_ul')
        if 'hover_bg' in kwargs:
            self._hover_bg = kwargs.pop('hover_bg')
        if 'fg_color' in kwargs:
            self._fg_color = kwargs.pop('fg_color')
        if 'bg_color' in kwargs:
            self._bg_color = kwargs.pop('bg_color')
        if 'popup_fg' in kwargs:
            self._popup_fg = kwargs.pop('popup_fg')
        if 'popup_bg' in kwargs:
            self._popup_bg = kwargs.pop('popup_bg')
        if 'popup_border' in kwargs:
            self._popup_border = kwargs.pop('popup_border')
        if 'popup_font' in kwargs:
            self._popup_font = kwargs.pop('popup_font')
        if 'show_url' in kwargs:
            self._show_url = kwargs.pop('show_url')
        if kwargs:
            raise ValueError(f'{list(kwargs.keys())} not supported.')
        
    def get_config(self) -> dict:
        return vars(TextboxLink())
