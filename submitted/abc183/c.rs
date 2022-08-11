use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        (n, k): (usize, i64),
        t: [[i64; n]; n]
    }
    let mut ans = 0;
    for path in (1..n).permutations(n - 1) {
        let mut time = t[0][path[0]] + t[path[n - 2]][0];
        let mut now = path[0];
        for next in path {
            time += t[now][next];
            now = next;
        }
        if time == k {
            ans += 1;
        }
    }
    println!("{}", ans);
}