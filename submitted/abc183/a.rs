use proconio::input;

fn main() {
    input! {
        x: i32
    }
    let mut ans = 0;
    if x >= 0 {
        ans = x
    }
    println!("{}", ans);
}