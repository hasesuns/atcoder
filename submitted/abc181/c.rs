use proconio::input;

fn main() {
    input! {
        n: usize,
        xy: [(i64, i64); n]
    }

    for i in 0..n {
        for j in (&i + 1)..n {
            for k in (&j + 1)..n {
                let dx1 = xy[j].0 - xy[i].0;
                let dx2 = xy[k].0 - xy[i].0;
                let dy1 = xy[j].1 - xy[i].1;
                let dy2 = xy[k].1 - xy[i].1;
                if dx2 * dy1 == dx1 * dy2 {
                    println!("Yes");
                    return;
                }
            }
        }
    }
    println!("No");
}