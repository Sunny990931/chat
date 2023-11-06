#讀取檔案並設立清單
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f :
		for line in f :
			lines.append(line.strip())
	return lines 


def convert(lines):
	person = None #預設值為無可作為宣告變數
	allen_word_count = 0
	allen_sticker_count = 0
	allen_pic_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_pic_count = 0
	for line in lines : #一行一行讀取
		s = line.split(' ')#split分割句子
		time = s[0]
		name = s[1]
		if name == 'Allen' :
			if s[2] == '貼圖':
				allen_sticker_count +=1
			elif s[2] == '圖片':
				allen_pic_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki' :
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片' :
				viki_pic_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen says', allen_word_count)
	print('allen send',allen_sticker_count, 'stickers')
	print('allen send', allen_pic_count, 'pictures')
	print('viki says', viki_word_count)
	print('viki send',viki_sticker_count, 'stickers')
	print('viki send', viki_pic_count, 'pictures')

		

	


def write_file(filename, lines):
	with open(filename, 'w') as f :
		for line in lines :
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()
#n=[2,6,6,8,4]
#n[:3]=前三個值=0~3的意思=2,6,6
#n[2:4]=2~3的意思=6,8
#n[-2:]=4,8