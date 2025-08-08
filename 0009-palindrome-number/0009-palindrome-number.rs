impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let s = x.to_string();
        let rev_s: String = s.chars().rev().collect();
        s == rev_s
    }
}