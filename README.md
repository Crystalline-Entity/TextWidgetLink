<h1 align="center">TextWidgetLink</h1>

<h3 align="center">Add highlighted URL link to a Text Widget.</h3>

```python
from TextWidgetLink import TextWidgetLink
text_widget_link = TextWidgetLink()

text_widget_link.add(text_widget=tb, the_text='Complex Numbers:', tag_name='Complex',
                     new_text='Complex Numbers',
                     popup_fg='red', popup_bg='lightgreen', popup_border='purple',
                     the_link='https://en.wikipedia.org/wiki/Complex_number')
text_widget_link.add(text_widget=tb, the_text='Base Numbers:', tag_name='Base', bg_color='gold',
                     the_link='https://en.wikipedia.org/wiki/Radix')
text_widget_link.add(text_widget=tb, the_text='Roman Numbers:', tag_name='Roman',
                     the_link='https://en.wikipedia.org/wiki/Roman_numerals')
text_widget_link.add(text_widget=tb, the_text='3.1415927', tag_name='pi',
                     the_link='https://en.wikipedia.org/wiki/Pi')
text_widget_link.add(text_widget=tb, the_text='[Email]', new_text='Email',
                     popup_font=('Courier New', 18), show_url=False,
                     tag_name='email', the_link='mailto:kevin.glentworth@gmail.com')
```
![Screenshot](https://github.com/Crystalline-Entity/TextboxLink/blob/main/textwidgetlink_messagebox.png)
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
