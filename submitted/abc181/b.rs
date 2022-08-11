use proconio::input;

fn calc_trapezium_sum(start: u64, end: u64) -> u64 {
    return (start + end) * (end - start + 1) / 2;
}

fn main() {
    input! {
        n: usize,
        ab: [(u64, u64); n],
    }
    let mut ans = 0;
    for (a, b) in ab {
        ans += calc_trapezium_sum(a, b)
    }

    println!("{:?}", ans);
}