use proconio::input;

fn main() {
    input! {
        n: usize,
        mut xy:[(f32,f32); n],
    }
    let mut ans = 0;
    for i in 0..n - 1 as usize {
        for j in i + 1..n as usize {
            let m = (xy[j].1 - xy[i].1) / (xy[j].0 - xy[i].0);
            if -1. <= m && m <= 1. {
                ans += 1
            }
        }
    }
    println!("{}", ans);
}