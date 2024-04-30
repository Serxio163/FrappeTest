import frappe


def on_field1_change(doc, method):
    # Эта функция будет вызвана, когда 'field1' изменится в указанном doc
    if doc.field1 == '1':
        doc.set_df_property('field2', 'options', ['A1', 'A2', 'A3'])
    elif doc.field1 == '2':
        doc.set_df_property('field2', 'options', ['B1', 'B2', 'B3'])
    elif doc.field1 == '3':
        doc.set_df_property('field2', 'options', ['C1', 'C2', 'C3'])

def on_field2_change(doc, method):
    # Эта функция будет вызвана, когда 'field2' изменится в указанном doc
    if doc.field2.endswith('1'):
     doc.field3 = 'Г'
    elif doc.field2.endswith('2'):
     doc.field3 = 'Д'
    elif doc.field2.endswith('3'):
     doc.field3 = 'Е'

# Добавить хуки, которые будут вызывать эти функции
frappe.custom_hooks = {
    'field1': {
        'on_change': on_field1_change,
    },
    'field2': {
        'on_change': on_field2_change,
    }
}
