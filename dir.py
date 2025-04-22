import tkinter as tk
import os


def traverse_tree(current_path, parent_node):
    # 获取目录下的文件列表
    files = os.listdir(current_path)

    # 遍历文件列表
    for file in files:
        # 获取文件的全路径
        file_path = os.path.join(current_path, file)

        # 判断是否为目录
        if os.path.isdir(file_path):
            # 如果是目录，创建一个新的节点
            node = tk.LabelFrame(parent_node, text=file)
            node.pack(side=tk.TOP, fill=tk.X)

            # 绑定事件，点击展开或关闭目录
            node.bind("<Button-1>", lambda event, node=node, file_path=file_path: toggle_tree(event, node, file_path))

            # 递归遍历子目录
            traverse_tree(file_path, node)
        else:
            # 如果是文件，创建一个新的标签
            label = tk.Label(parent_node, text=file)
            label.pack(side=tk.TOP, fill=tk.X)

def toggle_tree(event, node, file_path):
    # 判断节点下是否存在子节点
    children = node.winfo_children()
    if children:
        # 如果存在子节点，关闭子节点
        for child in children:
            child.destroy()
    else:
        # 如果不存在子节点，打开子节点
        traverse_tree(file_path, node)

# 创建窗口
window = tk.Tk()
window.title("本地目录树")
window.geometry("600x400")

# 创建根节点
root_node = tk.LabelFrame(window, text=os.getcwd())
root_node.pack(side=tk.TOP, fill=tk.X)

# 绑定事件，点击展开或关闭目录
root_node.bind("<Button-1>", lambda event, node=root_node, file_path=os.getcwd(): toggle_tree(event, node, file_path))

# 遍历目录树
traverse_tree(os.getcwd(), root_node)

# 运行窗口
window.mainloop()
