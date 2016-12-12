using Nettle

iv = "wtnhxymk"

function answer1()
  h = Hasher("MD5")
  answer = ""
  for i = 1:2^32
    update!(h, iv * string(i))
    hash = digest!(h)
    if hash[1] == 0 && hash[2] == 0 && hash[3] & 0xf0 == 0
      answer = answer * bytes2hex(hash)[6:6]
      if length(answer) == 8
        break
      end
    end
  end
  println(answer)
end

function answer2()
  h = Hasher("MD5")
  answer = "________"
  count = 0
  for i = 1:2^32
    update!(h, iv * string(i))
    hash = digest!(h)
    if hash[1] == 0 && hash[2] == 0 && hash[3] < 8 && answer[hash[3]+1] == '_'
      x = hash[3]
      answer = answer[1:x] * bytes2hex(hash)[7:7] * answer[x+2:end]
      count += 1
      if count == 8
        break
      end
    end
  end
  println(answer)
end

answer1()
answer2()