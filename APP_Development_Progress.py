import PySimpleGUIWeb as sg


table_list = [
    ['项目名称','进度'],
    ['门窗管理系统','True'],
    ['PnP_System','True']
]

layout = [
    [sg.Table(values=table_list,
              key='-Table-',
              text_color='black',
              display_row_numbers=True,
              row_header_text='编号')]

]

window = sg.Window('项目进展', layout=layout)
while True:
    event, values = window.read()
    print(event, values)
    if event == None or event == sg.WIN_CLOSED:
        break

window.close()

