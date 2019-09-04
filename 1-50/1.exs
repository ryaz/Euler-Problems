# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

defmodule Problem_1 do

  # O(n)
  def solver(number, maximum, sum) do
    IO.puts "#{number}, #{maximum}, #{sum}"
    if number > maximum do
      sum
    else
      if rem(number, 5) == 0 or rem(number, 3) == 0 do
        solver(number + 1, maximum, sum + number)
      else
        solver(number + 1, maximum, sum)
      end
    end
  end

end

IO.puts Problem_1.solver(0, 999, 0)