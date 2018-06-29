d1={}
class Trie(object):

    def add_word(self, word):
        global d1
        cur = d1
        nwrd = False
        for i in word:
            if i not in cur:
                nwrd = True
                cur.update({i:{}})
            cur= cur[i]
        if "End Of Word" not in cur:
            nwrd = True
            cur.update({"End Of Word":{}})
        return nwrd
