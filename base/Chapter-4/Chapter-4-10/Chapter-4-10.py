txt='A组-优秀；B组-良好；C组-优秀；D组-优秀' #被替换的字符串。
print(txt.replace('优秀','晋级')) #将所有'优秀'替换为'晋级'。
print(txt.replace('优秀','晋级',1)) #将前1个'优秀'替换为'晋级'。
print(txt.replace('优秀','晋级',2)) #将前2个'优秀'替换为'晋级'。