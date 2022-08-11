use proconio::input;

fn main() {
    input! {
        (a, b): (u64, u64)
    }
    let max = 2 * a + 100;
    let ans = max - b;
    println!("{}", ans);
}