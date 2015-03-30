(defn multiple-of-x? [x]
  (fn [n] (zero? (rem n x))))

(map #(cond
            ((every-pred (multiple-of-x? 3) (multiple-of-x? 5)) %) "FizzBuzz"
            ((multiple-of-x? 3) %) "Fizz"
            ((multiple-of-x? 5) %) "Buzz" 
            :else %) (range 1 100))
