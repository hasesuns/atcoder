use proconio::input;

fn main() {
    input! {
        (sx, sy, gx, gy): (f64, f64, f64, f64)
    }
    let slop = (-gy - sy) / (gx - sx);
    let ans = -sy / slop + sx;
    println!("{}", ans);
}