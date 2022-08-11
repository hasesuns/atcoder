use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [u64; n],
    }
    let mut ans = a[0];
    let mut max_num = 1;
    for candi in 2..=1000 {
        let mut cnt = 0;
        for aa in &a {
            if aa % candi == 0 {
                cnt += 1
            }
        }
        if cnt > max_num {
            ans = candi;
            max_num = cnt;
        }
    }
    println!("{}", ans);
}