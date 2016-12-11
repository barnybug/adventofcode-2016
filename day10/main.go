package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var reNumber = regexp.MustCompile(`\d+`)
var reDestination = regexp.MustCompile(`(bot|output)`)

type Bot struct {
	input chan int
}

func newBot() *Bot {
	return &Bot{input: make(chan int, 2)}
}

func main() {
	var bots []*Bot
	for i := 0; i < 210; i += 1 {
		bots = append(bots, newBot())
	}
	outputs := make([]chan int, 35)
	for i := 0; i < len(outputs); i += 1 {
		outputs[i] = make(chan int, 1)
	}

	f, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		s := scanner.Text()
		var nums []int
		for _, str := range reNumber.FindAllString(s, -1) {
			n, _ := strconv.Atoi(str)
			nums = append(nums, n)
		}

		if strings.HasPrefix(s, "value") {
			bots[nums[1]].input <- nums[0]
		} else {
			dests := reDestination.FindAllString(s, -1)
			bot := bots[nums[0]]
			// create a bot goroutine
			go func() {
				a := <-bot.input
				b := <-bot.input
				if a > b {
					t := a
					a = b
					b = t
				}
				if a == 17 && b == 61 {
					fmt.Println("Answer #1:", nums[0])
				}
				if dests[1] == "bot" {
					bots[nums[1]].input <- a
				} else {
					outputs[nums[1]] <- a
				}
				if dests[2] == "bot" {
					bots[nums[2]].input <- b
				} else {
					outputs[nums[2]] <- b
				}
			}()
		}
	}

	answer2 := <-outputs[0] * <-outputs[1] * <-outputs[2]
	fmt.Println("Answer #2:", answer2)
}
