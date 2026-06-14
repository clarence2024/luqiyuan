import os

def main():
    files = sorted([f for f in os.listdir('.') if f.startswith('chapter_') and f.endswith('.xhtml')])
    print(f'文件总数: {len(files)}')
    
    titles_modified = []
    dates_added = []
    no_date = []
    
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
            if '<title>第' in content:
                titles_modified.append(f)
            if '<p class="center">' in content and '年' in content:
                dates_added.append(f)
            else:
                no_date.append(f)
    
    print(f'标题已修改: {len(titles_modified)}')
    print(f'日期已添加: {len(dates_added)}')
    if no_date:
        print(f'\n未找到日期的文件: {no_date}')

if __name__ == '__main__':
    main()