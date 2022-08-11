use proconio::input;

fn main() {
    input! {
        (n, m): (i64, usize),
        mut a: [i64; m]
    }

    if m == 0 {
        println!("1");
        return;
    }

    if n == m as i64 {
        println!("0");
        return;
    }

    a.sort();
    let mut prev_blue: i64 = 0;
    let mut best_k = 10i64.pow(9);
    for aa in &a {
        if prev_blue + 1 != *aa {
            best_k = std::cmp::min(best_k, *aa - prev_blue - 1)
        }
        prev_blue = *aa;
    }
    if prev_blue != n {
        best_k = std::cmp::min(best_k, n - prev_blue);
    }

    let mut ans = 0;
    prev_blue = 0;
    for aa in a {
        if prev_blue + 1 != aa {
            ans += (aa - prev_blue - 1 + (best_k - 1)) / best_k;
        }
        prev_blue = aa;
    }
    ans += (n - prev_blue + (best_k - 1)) / best_k;
    println!("{}", ans);
}