use proconio::input;

fn main() {
    input! {
        l: u64
    }
    let mut ans = 1;
    for i in (1..=11) {
        ans *= l - i;
        ans /= i
    }

    println!("{:?}", ans);
}