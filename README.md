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
<div align='center'>

<h3 align='center'>Parameters for the initial call to textbox_link<h3>

  | **Parameter** | **Description** | **Default** |
  | --- | --- | --- |
  | underline | Underline text | True |
  | underlinefg | Underline colour | 'blue' |
  | hover_ul | Text colour when mouse hovers over text | 'green' |
  | hover_bg | Backgruond colour when mouse hovers over text | 'orange' |
  | fg_color | Highlighted text foreground colour | 'blue' |
  | bg_color | Highlighted text background colour | 'yellow' |
  | show_url | Show URL in popup when mouse hovers over highlighted text | True |
  | popup_fg | Foreground colour of URL popup | 'blue' |
  | popup_bg | background colour of URL popup | 'lightyellow' |
  | popup_border | border collur of URL popup |  'red' |
  | popup_font | URL popup font | ('Code New Roman', 13) |
