from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem,QMainWindow,QDialog, QDialogButtonBox, QVBoxLayout,QHBoxLayout,QWidget,QComboBox,QLabel,QTreeWidgetItem
import sys

def create_combobox_widget(tree_widget,tree_item_widget,phasename,options):
    print("create combobox widget")
    container_widget = QWidget()
    select_layout = QHBoxLayout()
    select_label = QLabel(phasename)
    select_combo = QComboBox()

    select_combo.addItem("None")
    for option in options:
        select_combo.addItem(option)
    select_combo.currentTextChanged.connect(lambda _:on_connect_validation(tree_widget,tree_item_widget,phasename,select_combo.currentText()))
    select_combo.setCurrentIndex(0)
    select_layout.addWidget(select_label)
    select_layout.addWidget(select_combo)
    container_widget.setLayout(select_layout)
    return container_widget

def create_validation_label(tree_widget:QTreeWidget,tree_item_widget,text,style):
    print("validation label")
    label = QLabel()
    label.setText(text)
    label.setStyleSheet(style)
    tree_widget.setItemWidget(tree_item_widget,1,label)

def on_connect_validation(tree_widget,tree_item_widget,phase_name,anim_name):
    print(phase_name,anim_name)
    print("validate")
    if anim_name == "a1":
        label = QLabel()
        label.setText(f"{phase_name} becomes anim {anim_name}")
        label.setStyleSheet("color: yellow;")
        tree_widget.setItemWidget(tree_item_widget,1,label)
    elif anim_name == "a2":
        label = QLabel()
        label.setText(f"Invalid anim added {anim_name}")
        label.setStyleSheet("color: red;")
        tree_widget.setItemWidget(tree_item_widget,1,label)
    elif anim_name == "a3":
        label = QLabel()
        label.setText("\u2714")
        label.setStyleSheet("color: green;")
        tree_widget.setItemWidget(tree_item_widget,1,label)
    else:
        label = QLabel()
        label.setText("")
        label.setStyleSheet("color: green;")
        tree_widget.setItemWidget(tree_item_widget,1,label)


def accept(app):
    print("accept")
    print("exit2")
    sys.exit(1)

def reject(app):
    print("reject")
    print("exit3")
    sys.exit(0)

def main():
    actors = ["test1","test2","test3"]
    phases = ["phase1","phase2","phase3","phase4","phase5"]
    anims_available = ["a1","a2","a3","a4","a5"]
    test_anims = {
        "test1":["t1","t2"],
        "test2":[],
        "test3":[]
    }
    test_struct_anims = {
        "test1":{"struct1":["anim1","anim2","anim3","anim4"]},
        "test2":{"struct1":["anim1"],"struct2":["anim1","anim2"],"struct3":["anim4"]},
        "test3":{"struct1":["anim1"],"struct2":["anim1"]}
    }
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("test tree widget")
    window.resize(800,600)

    layout = QVBoxLayout()
    tree_widget = QTreeWidget()
    tree_widget.setColumnCount(2) # Example with two columns
    tree_widget.setHeaderLabels(["Name", "Description"])

    # Top-level item
    for each_actor in actors:
        parent_item = QTreeWidgetItem([each_actor])
        tree_widget.addTopLevelItem(parent_item)
        
        # Anims Child item
        anims_child_item = QTreeWidgetItem(["test Anims"])
        parent_item.addChild(anims_child_item)

        for phase in phases:
            container_widget = QTreeWidgetItem()
            anims_child_item.addChild(container_widget)
            npc_anims_combo_widget = create_combobox_widget(tree_widget,container_widget,phase,anims_available)
            tree_widget.setItemWidget(container_widget,0,npc_anims_combo_widget)
            create_validation_label(tree_widget,container_widget)
        
        # Struct anims Child item
        struct_anims_child_item = QTreeWidgetItem(["test Struct Anims"])
        parent_item.addChild(struct_anims_child_item)

        for key,values in test_struct_anims.items():
            if key == each_actor:
                for struct_name, anims in values.items():
                    struct_anims_item =  QTreeWidgetItem([struct_name])
                    struct_anims_child_item.addChild(struct_anims_item)
                    for phase in phases:
                        container_widget = QTreeWidgetItem()
                        struct_anims_item.addChild(container_widget)
                        test_anims_combo_widget = create_combobox_widget(tree_widget,container_widget,phase,anims_available)
                        tree_widget.setItemWidget(container_widget,0,test_anims_combo_widget)
                        create_validation_label(tree_widget,container_widget)
    
    button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
    button_box.accepted.connect(lambda : accept(app))
    button_box.rejected.connect(lambda : reject(app))

    layout.addWidget(tree_widget)
    layout.addWidget(button_box)

    container_widget = QWidget()
    container_widget.setLayout(layout)
    window.setCentralWidget(container_widget)
    window.show()
    tree_widget.expandAll()
    tree_widget.header().resizeSection(0, 300)
    print("exit")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()