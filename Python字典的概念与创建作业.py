"""
假如已知小明、小红、小亮三个同学的语文、数学、英语成绩分别为（85,96,88）、(72,80,91)、
(83,69,75)，如何使用Python字典将姓名、学科、成绩做对应，并计算谁的总分最高。
"""
# 创建一个包含学生姓名和对应成绩的字典
scores = {
    '小明': {'语文': 85, '数学': 96, '英语': 88},
    '小红': {'语文': 72, '数学': 80, '英语': 91},
    '小亮': {'语文': 83, '数学': 69, '英语': 75}
}

# 计算每个学生的总分
total_scores = {name: sum(subject_scores.values()) for name, subject_scores in scores.items()}
print(total_scores)
# 找出总分最高的学生
max_score_student = max(total_scores, key=total_scores.get)

# 输出每个学生的总分
for name, total_score in total_scores.items():
    print(f"{name}的总分为：{total_score}")

# 输出总分最高的学生
print(f"总分最高的学生是：{max_score_student}，总分为：{total_scores[max_score_student]}")