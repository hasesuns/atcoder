use proconio::input;

fn main() {
    input! {
        (a, b): (i64, i64),
        (c, d): (i64, i64)
    }
    let ans = a * d - b * c;
    println!("{}", ans);
}