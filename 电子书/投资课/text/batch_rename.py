# -*- coding: utf-8 -*-
import re
import os

def convert_chapter_number(filename):
    """将章节号从3位数改为2位数"""
    filepath = os.path.join(r'e:\code\luqiyuan\电子书\投资课\text', filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replacer_3to2(match):
        """将3位数章节号转为2位"""
        num = match.group(2)
        return match.group(1) + str(int(num)).zfill(2) + match.group(3)
    
    # 修改 <title>第001节 xxx</title> -> <title>第01节 xxx</title>
    content = re.sub(r'(<title>第)(\d{3})(节)', replacer_3to2, content)
    
    # 修改 <h1...>第001节 xxx</h1> -> <h1...>第01节 xxx</h1>
    content = re.sub(r'(<h1[^>]*>第)(\d{3})(节)', replacer_3to2, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # 验证修改
    title_match = re.search(r'<title>第(\d{2})节', content)
    h1_match = re.search(r'<h1[^>]*>第(\d{2})节', content)
    
    if title_match and h1_match:
        return True, title_match.group(1), h1_match.group(1)
    return False, None, None

def main():
    print("Starting batch modify chapter title format...")
    print("=" * 50)
    
    success_count = 0
    fail_count = 0
    
    for i in range(1, 65):
        filename = f'chapter_{i:03d}.xhtml'
        try:
            ok, title_num, h1_num = convert_chapter_number(filename)
            if ok:
                print(f"[OK] {filename}: title={title_num}, h1={h1_num}")
                success_count += 1
            else:
                print(f"[FAIL] {filename}: modify failed or chapter number not found")
                fail_count += 1
        except Exception as e:
            print(f"[ERROR] {filename}: {e}")
            fail_count += 1
    
    print("=" * 50)
    print(f"Done! Success: {success_count}, Failed: {fail_count}")

if __name__ == '__main__':
    main()
