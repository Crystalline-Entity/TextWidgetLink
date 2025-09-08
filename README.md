<h1 align="center">TextboxLink</h1>

<h3 align="center">Add highlighted URL link to a TextBox.</h3>

```python
from TextboxLink import TextboxLink
textbox_link = TextboxLink()

textbox_link.add(text_widget=tb, the_text='Complex Numbers:', tag_name='Complex',
                new_text='Complex Numbers',
                popup_fg='red', popup_bg='lightgreen', popup_border='purple',
                the_link='https://en.wikipedia.org/wiki/Complex_number')
textbox_link.add(text_widget=tb, the_text='Base Numbers:', tag_name='Base',
                the_link='https://en.wikipedia.org/wiki/Radix')
textbox_link.add(text_widget=tb, the_text='Roman Numbers:', tag_name='Roman',
                the_link='https://en.wikipedia.org/wiki/Roman_numerals')
textbox_link.add(text_widget=tb, the_text='3.1415927', tag_name='pi',
                the_link='https://en.wikipedia.org/wiki/Pi')
textbox_link.add(text_widget=tb, the_text='[EMail]', new_text='EMail',
                popup_font=('Courier New', 18), show_url=False,
                tag_name='email', the_link='mailto:username@domain')
```
![Screenshot](https://github.com/Crystalline-Entity/TextboxLink/blob/main/textboxlink_messagebox.png)
<br>
<h2 align='center'> OPTIONS </h2>
<div align='left'>

Parameters for the initial call to textbox_link. These are the defaults for all future calls.

  | **Parameter** | **Description** | **Default** |
  | --- | --- | --- |
  | underline | Underline text | True |
  | underlinefg | Underline colour | 'blue' |
  | hover_ul | Text colour when mouse hovers over text | 'green' |
  | hover_bg | Background colour when mouse hovers over text | 'orange' |
  | fg_color | Highlighted text foreground colour | 'blue' |
  | bg_color | Highlighted text background colour | 'yellow' |
  | show_url | Show URL in popup when mouse hovers over highlighted text | True |
  | popup_fg | Foreground colour of URL popup | 'blue' |
  | popup_bg | background colour of URL popup | 'lightyellow' |
  | popup_border | border colour of URL popup |  'red' |
  | popup_font | URL popup font | ('Code New Roman', 13) |

Parameters for calls to .add to create highlighted text.
These options are used to over-ride the options from the initial call above. These options apply only to this
call and are not saved.

  | **Parameter** | **Description** |
  | --- | --- |
  | text_widget |  The name of the text widget to apply highlights to |
  | the_text | The text in the widget to highlight |
  | tag_name | The name of the tag to use for this highlight|
  | the_link | The URL to assign to the text |
  | new_text | Replacement text for the_text. Used if the_text has id options |
  | underline | Underline text |
  | underlinefg | Underline colour |
  | hover_ul | Text colour when mouse hovers over text |
  | hover_bg | Background colour when mouse hovers over text |
  | fg_color | Highlighted text foreground colour |
  | bg_color | Highlighted text background colour |
  | show_url | Show URL in popup when mouse hovers over highlighted text |
  | popup_fg | Foreground colour of URL popup |
  | popup_bg | background colour of URL popup |
  | popup_border | border colour of URL popup |
  | popup_font | URL popup font, specified as ('family', size) |

To change the default values for future calls, use .config and set the values.
