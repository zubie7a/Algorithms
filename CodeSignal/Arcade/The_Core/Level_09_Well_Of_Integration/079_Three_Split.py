# https://app.codesignal.com/arcade/code-arcade/well-of-integration/QmK8kHTyKqh8xDoZk
def threeSplit(numbers):
   # From a list of numbers, cut into three pieces such that each
   # piece contains an integer, and the sum of integers in each
   # piece is the same.

   # We know that the total sum of elements in the array is divisible by 3.
   # So any 3 segments it can be divided into must have sum total/3.
   total = sum(numbers)
   third = total / 3
   # The count of starts, this is, places where it adds to a third.
   start_count = 0
   # Acum so far of values in the array.
   acum_sum = 0
   # Result which will hold the amount of ways the array can be split into 3 equally.
   result = 0
   for idx in range(len(numbers) - 1):
      # Keep accumulating values.
      acum_sum += numbers[idx]
      # A second splitting point is if up to this point it adds to two thirds.
      # Checked before the start point for the case in which a third of the total
      # is equal to two thirds, because the total added up to 0. Also for a second
      # splitting point to be valid, there has to be at least one starting point.
      if acum_sum == 2 * third and start_count > 0:
         # Any "second splitting point" found will work with any of the previously
         # found "starting splitting points", so add up the amount of such points
         # found until the current one.
         result += start_count
      # A starting splitting point is if up to this point it adds up to a third.
      if acum_sum == third:
         start_count += 1

   return result
