package main

import "testing"

func TestHello(t *testing.T) {
	got := Hello("pat")
	want := "Hello, pat"

	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}
