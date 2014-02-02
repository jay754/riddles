def main
	results = []

	for i in 2..100
		for j in 2..100
			results.push(i**j)
		end
	end

	puts results.uniq.length
end

main()