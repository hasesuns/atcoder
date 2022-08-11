use proconio::input;

fn main() {
    input! {
        n: usize,
        ab: [(u64, u64); n]
    }
    let mut val: Vec<_> = ab.iter().map(|x| 2 * x.0 + x.1).collect();
    val.sort();
    val.reverse();
    let aoki = ab.iter().fold(0, |aoki, x| aoki + x.0);
    let mut ans = 0;
    let mut takahashi = 0;
    for v in val.iter().take(n) {
        takahashi += v;
        ans += 1;
        if takahashi > aoki {
            break;
        }
    }
    println!("{}", ans);
}