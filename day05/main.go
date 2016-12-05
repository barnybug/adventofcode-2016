package main

import (
	"crypto/md5"
	"fmt"
)

var key = []byte("wtnhxymk")

func hasher(n int, result chan []byte) {
	h := md5.New()
	for i := n; true; i += 4 {
		h.Write(key)
		h.Write([]byte(fmt.Sprint(i)))
		hash := h.Sum([]byte{})
		if hash[0] == 0 && hash[1] == 0 && hash[2]>>4 == 0 {
			result <- hash
		}
		h.Reset()
	}
}

func answer1() {
	answer := ""
	result := make(chan []byte, 4)
	for n := 0; n < 4; n += 1 {
		go hasher(n, result)
	}

	for hash := range result {
		answer += fmt.Sprintf("%0x", hash[2])
		fmt.Println(answer)
		if len(answer) == 8 {
			break
		}
	}

	fmt.Println(answer)
}

func answer2() {
	result := make(chan []byte, 4)
	for n := 0; n < 4; n += 1 {
		go hasher(n, result)
	}

	count := 0
	done := make([]bool, 8)
	digits := make([]byte, 8)
	for hash := range result {
		pos := hash[2]
		if pos < 8 && !done[pos] {
			done[pos] = true
			digits[pos] = hash[3] >> 4
			count += 1
		}
		if count == 8 {
			break
		}
	}

	answer := ""
	for _, ch := range digits {
		answer += fmt.Sprintf("%0x", ch)
	}
	fmt.Println(answer)
}

func main() {
	answer2()
}
