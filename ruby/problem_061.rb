class Problem61

  def initialize
    @result = nil

    @tri = Proc.new { |n| (n * (n + 1)) / 2 }
    @squ = Proc.new { |n| n ** 2 }
    @pen = Proc.new { |n| (n * (3 * n - 1)) / 2 }
    @hex = Proc.new { |n| n * (2 * n - 1) }
    @hep = Proc.new { |n| (n * (5 * n - 3)) / 2 }
    @oct = Proc.new { |n| n * (3 * n - 2) }

    @poly_nums = [
      poly_set(@tri),
      poly_set(@squ),
      poly_set(@pen),
      poly_set(@hex),
      poly_set(@hep),
      poly_set(@oct)
    ]
  end

  public

  def run()
    get_cyclic_set([], nil, @poly_nums)
    puts @result.map(&:to_i).inject(:+)
  end

  private

  # Get figurate set as array of 4-digit strings so substrings can be tested
  # {Proc} f Polynomial equation
  def poly_set(f)
    (0..200).to_a.map { |n| f.call(n).to_s if f.call(n).to_s.length == 4}.compact!
  end

  # Given there is only one set of six cyclic 4-digit numbers
  # {Array<String>} cyclic_set Accumulated cyclic set
  # {String} prev_digit_str The four digit string from the previous iteration
  # {Array<Array<String>>} poly_sets Array of remaining poly arrays
  def get_cyclic_set(cyclic_set, prev_digit_str, poly_sets)
    return if @result

    if poly_sets.empty? && prev_digit_str[2..3] == cyclic_set[0][0..1]
      @result = cyclic_set
    end

    if cyclic_set.empty?
      poly_sets.pop.each do |prev_digit_str|
        get_cyclic_set([prev_digit_str], prev_digit_str, poly_sets)
      end
    else
      poly_sets.each do |poly_set|
        poly_set.each do |digit_str|
          if prev_digit_str[2..3] == digit_str[0..1]
            new_cyclic_set = cyclic_set.map(&:dup) << digit_str
            new_poly_sets = poly_sets.select { |s| s != poly_set }
            get_cyclic_set(new_cyclic_set, digit_str, new_poly_sets)
          end
        end
      end
    end
  end
end

problem = Problem61.new
problem.run
