use proconio::input;

fn main() {
    input! {
        n: usize,
        mut a: [i64; n]
    };
    a.sort();
    let cumsum = a
        .iter()
        .scan(0, |cum, x| {
            *cum += x;
            Some(*cum)
        })
        .collect::<Vec<i64>>();

    let mut ans = 0;
    for i in 1..n {
        ans += i as i64 * a[i] - cumsum[i - 1];
    }
    println!("{}", ans);
}