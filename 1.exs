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