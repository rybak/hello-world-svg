
output.svg: begin.svg generated.svg end.svg
	cat $^ >$@

output-bg.svg: begin.svg background.svg generated.svg end.svg
	cat $^ >$@

generated.svg: generate.py
	./generate.py >$@

