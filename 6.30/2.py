cat words.txt | tr -s ' ' '\n' | sed 's/^[ \t]*//g' | sed 's/[ \t]*$//g' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
# https://leetcode.cn/problems/word-frequency/submissions/
