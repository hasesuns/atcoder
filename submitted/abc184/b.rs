use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        (n, x): (usize, usize),
        s: Chars,
    }
    let mut ans = x;
    for ss in s {
        if ss == 'x' && ans > 0 {
            ans -= 1
        } else if ss == 'o' {
            ans += 1
        }
    }
    println!("{}", ans);
}