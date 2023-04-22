#https://leetcode.cn/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        cur_len = 0 # 当前行已经填了多少字符
        last_start = 0 # 上一行的第一个单词在 words 中的位置
        for i in range(n):
            if cur_len + len(words[i]) + i - last_start > maxWidth: # 如果加入该单词会超过 maxWidth，则该单词不能加入当前行
                word_num = i - last_start
                space_num = maxWidth - cur_len
                if word_num == 1: # 如果当前行只有一个单词，则左对齐并在末尾添加空格
                    res.append(words[last_start] + ' ' * (maxWidth - cur_len))
                else:
                    avg_space = space_num // (word_num - 1) # 平均每个单词之间应该加入的空格数量
                    extra_space = space_num % (word_num - 1) # 剩余的空格数量，需要从左边开始依次分配
                    line = ''
                    for j in range(last_start, i):
                        line += words[j]
                        if j < i - 1:
                            line += ' ' * avg_space # 平均分配的空格
                            if extra_space > 0:
                                line += ' ' # 左侧需要多加 1 个空格
                                extra_space -= 1
                    res.append(line)
                cur_len = 0
                last_start = i
            cur_len += len(words[i])
        # 处理最后一行
        last_line = ' '.join(words[last_start:])
        last_line += ' ' * (maxWidth - len(last_line)) # 左对齐，末尾补充空格
        res.append(last_line)
        return res

