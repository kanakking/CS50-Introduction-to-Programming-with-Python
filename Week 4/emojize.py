import emoji

emo = input("Input: ").strip()
emoj = emoji.emojize(emo, language = "alias")

print(f"{emoj}")