card=open( 'novel.txt', encoding='utf8' ) #gets info from the text inside novel.txt
counter=[]
unique_items=[]
not_kanji=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ヂ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'パ', 'ピ', 'プ', 'ペ', 'ポ', 'っ', 'ッ', '.', ',', '。', '、', '：', ':', "'", '(', ')', '１', '２', '３', '４', '５', '６', '７', '８', '９', '０', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '{', '}', '!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '\\', '|', '＊','ー']
card_word_freq=open('frequency.txt','w',encoding='utf8') #creates a new .txt file
for character in card.read():
    counter.append(character) #each character is an item in the counter list
for character in counter:
    if character not in unique_items and character not in not_kanji: #creates a list that contains each non_kanji 1 time
        unique_items.append(character)
print(unique_items) #testing, if non-kanji cases are not meaningful (half width kana, random unicode) the program works fine. else, append to not kanji later.
for uniqe_item in unique_items: #iterates through all unique kanji
    unique_item_amount=counter.count(uniqe_item) #counts the amount of times each one appears in the counter list
    card_word_freq.write(f'"{uniqe_item}" appears {unique_item_amount} times in the given text.\n') #writes the frequency of each kanji character.
card.close()
card_word_freq.close()
#letters=str(input('Enter letters: '))
#e=[]
#for letter in letters:
#   e.append(f"{letter}")
#print(e)