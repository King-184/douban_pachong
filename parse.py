import os
from bs4 import BeautifulSoup

# 使用原始字符串
dest_dir = "C:/Users/Lenovo/Desktop/codes/software_class/douban_pachong/get_data"

for html_file in os.listdir(dest_dir):
    print(html_file.title())
    # 使用 os.path.join 正确拼接路径
    file_path = os.path.join(dest_dir, html_file)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
            print(html)
            # 抽取文件内容
            soup = BeautifulSoup(html, 'lxml')
            movie_list = soup.find('ol', class_='grid_view').find_all('li')
            for movie in movie_list:
                title = movie.find('div', class_='hd').find('span', class_='title').get_text()
                rating_num = movie.find('div', class_='bd').find('div').find('span', class_='rating_num').get_text()
                comment_num = movie.find('div', class_='bd').find('div').find_all('span')[-1].get_text()
                directors = movie.find('div', class_='bd').find('p').get_text()
                link = movie.find('div', class_='item').find('div', class_='pic').find('a').get('href')
                pic = movie.find('div', class_='item').find('div', class_='pic').find('a').find('img').get('src')
                print(title, rating_num, comment_num, directors, link, pic)
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到，请检查路径和文件名。")
    except Exception as e:
        print(f"处理文件 {file_path} 时出现错误: {e}")