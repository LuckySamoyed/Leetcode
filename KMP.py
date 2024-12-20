def get_next(s):
    # s : str -> next : List
    # s : "aabaafaafda"
    # next : [0, 1, 0, 1, 2, 0, 1, 2, 0, 0, 1]
    s = list(s)
    j = 0               # 前缀末尾
    next = [0]          # 第一个元素没有最长公共前缀后缀，初始化0
    for i in range(1, len(s)):   # 后缀末尾
        while s[i] != s[j] and j > 0:   # 不匹配那就让j往回退
            j = next[j - 1]               # 看j前面的字符串的最长公共前后缀长度，说明从开头有这个长度个数跟末尾一样，那就移动那些位置再比较，也就是指到其索引下标
        if s[i] == s[j]:    # 相等的话j加1
            j += 1
        next.append(j)      # next[i] = j，就是从开头到i(包括i)的最长公共前后缀长度，为j
    return next

# KMP算法：在文本串中匹配模式串
# 文本串
# 模式串
# 模式串的next数组
# 一个指针指向文本串开头，一个指向模式串开头，匹配就同时右移
# 不匹配就把模式串的指针往回调，如当前在索引k处不匹配，那就找0->k-1的最长xxx，也就是next[k-1]的值，
# 说明前0->k-1有next[k-1]跟后缀一样，就不用从头比较，只需比较后面不一样的，也就是移到索引next[k-1]处继续比较
def KMP(text,moshi):
    next = get_next(moshi)
    print(next)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != moshi[j]:
            j = next[j - 1]
        if text[i] == moshi[j]:
            j += 1
        if j == len(moshi):
            return i - j + 1
    return -1

    '''
    m = 0
    t = 0
    while t < len(text):
        if text[t] == moshi[m]:
            m += 1
            t += 1
            if m == len(moshi):
                return t - m
            continue
        elif m > 0:
            m = next[m - 1]
        if m == 0 and text[t] != moshi[m]:
            t += 1
    return -1
    '''
ss = "aabaafaafda"
print(get_next(ss))
text = "aabaabaafa"
moshi = "aabaaf"
print(KMP(text,moshi))
print(KMP("leetcode","leeto"))

